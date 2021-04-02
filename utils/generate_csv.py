import click
import csv
from datetime import datetime, timedelta
import random


@click.command()
@click.option('--out_file', default='test_file', help='name of output file')
def generate_csv(out_file):
    with open(out_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User"])

        for index in range(1, 10):
            writer.writerow([f"user{index}@gmail.com"])

        writer.writerow(["SubscriptionType"])

        for index in range(1, 10):
            writer.writerow([f"type{index}", f"{index}"])

        writer.writerow(["Artist"])

        for index in range(1, 10):
            writer.writerow([f"artist{index}", f"{generate_date()}"])

        writer.writerow(["Playlist"])

        for index in range(1, 10):
            writer.writerow([f"playlist{index}", f"user{index}@gmail.com"])

        writer.writerow(["Subscription"])

        for index in range(1, 10):
            writer.writerow(
                [f"{generate_date().date()}",
                 f"{generate_date().date()}",
                 f"{generate_bool()}",
                 f"user{index}@gmail.com",
                 ]
            )

        writer.writerow(["Album"])

        for index in range(1, 10):
            writer.writerow(
                [f"album{index}",
                 f"{index}",
                 f"{generate_date().time()}",
                 f"artist{index}"]
            )

        writer.writerow(["Song"])

        for index in range(1, 10):
            writer.writerow(
                [f"song{index}",
                 f"{generate_date().time()}",
                 f"artist{index}",
                 f"album{index}"]
            )

        writer.writerow(["PlaylistHasSong"])

        for index in range(1, 10):
            writer.writerow(
                [f"{generate_bool()}",
                 f"{generate_date().time()}",
                 f"playlist{index}",
                 f"song{index}"]
            )


def generate_date(min_year=1990, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def generate_bool():
    return random.choice([True, False])


if __name__ == "__main__":
    generate_csv()
