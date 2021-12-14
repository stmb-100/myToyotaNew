import json
import asyncio
from mytoyota.client import MyT

username = "stefan.muehlbauer@smb-soft.de"
password = "12stefan34"
locale = "de-de"

# Get supported regions.
print(MyT.get_supported_regions())

client = MyT(username=username, password=password, locale=locale, region="europe")


async def get_information():
    print("Logging in...")
    await client.login()

    print("Retrieving cars...")
    # Returns cars registered to your account + information about each car.
    cars = await client.get_vehicles()

    for car in cars:

        # Returns live data from car/last time you used it as an object.
        vehicle = await client.get_vehicle_status(car)


        # You can either get them all async (Recommended) or sync (Look further down).
        data = await asyncio.gather(
            *[
                client.get_driving_statistics(vehicle.vin, interval="day"),
                client.get_driving_statistics(vehicle.vin, interval="isoweek"),
                client.get_driving_statistics(vehicle.vin),
                client.get_driving_statistics(vehicle.vin, interval="year"),
            ]
        )

        # You can deposit each result into premade object holder for statistics. This will make it easier to use in your code.

        vehicle.statistics.daily = data[0]
        vehicle.statistics.weekly = data[1]
        vehicle.statistics.monthly = data[2]
        vehicle.statistics.yearly = data[3]


        # You can access odometer data like this:
        mileage = vehicle.odometer.mileage
        # Or retrieve the energy level (electric or gasoline)
        fuel = vehicle.energy.level
        # Or Parking information:
        latitude = vehicle.parking.latitude


        # Pretty print the object. This will provide you with all available information.
        print(json.dumps(vehicle.as_dict(), indent=3))


        # -------------------------------
        # All data is return in an object.
        # -------------------------------

        # Returns live data from car/last time you used it.
        vehicle = await client.get_vehicle_status(car)
        print(vehicle.as_dict())

        # Stats returned in a dict
        daily_stats = await client.get_driving_statistics(vehicle.vin, interval="day")
        print(daily_stats.as_list())

        # Stats returned in json.
        weekly_stats = await client.get_driving_statistics(vehicle.vin, interval="isoweek")
        print(weekly_stats.as_list())

        # ISO 8601 week stats
        iso_weekly_stats = await client.get_driving_statistics(vehicle.vin, interval="isoweek")
        print(iso_weekly_stats.as_list)

        # Monthly stats is returned by default
        monthly_stats = await client.get_driving_statistics(vehicle.vin)
        print(monthly_stats.as_list())

        #Get year to date stats.
        yearly_stats = await client.get_driving_statistics(vehicle.vin, interval="year")
        print(yearly_stats.as_list())


loop = asyncio.get_event_loop()
loop.run_until_complete(get_information())
loop.close()
