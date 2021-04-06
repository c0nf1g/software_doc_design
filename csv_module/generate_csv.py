import click
import csv
from datetime import datetime, timedelta
import random


@click.command()
@click.option('--out_file', default='test_file', help='name of output file')
def generate_csv(out_file):
    with open(f"{out_file}.csv", "w", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["User"])
        writer.writerow(["id", "apple_id"])

        for index in range(1, 200):
            writer.writerow([f"{index}", f"user{index}@gmail.com"])

        writer.writerow(["SubscriptionType"])
        writer.writerow(["id", "name", "price"])

        for index in range(1, 200):
            writer.writerow([f"{index}", f"type{index}", f"{index}"])

        writer.writerow(["Artist"])
        writer.writerow(["id", "name", "creation_date"])

        for index in range(1, 200):
            writer.writerow([f"{index}", f"artist{index}", f"{generate_date().strftime('%Y-%m-%d')}"])

        writer.writerow(["Playlist"])
        writer.writerow(["id", "name", "user_id"])

        for index in range(1, 200):
            writer.writerow([f"{index}", f"playlist{index}", f"{index}"])

        writer.writerow(["Subscription"])
        writer.writerow(["id", "active_until", "last_payment", "is_active", "user_id", "subscription_type_id"])

        for index in range(1, 200):
            writer.writerow(
                [f"{index}",
                 f"{generate_date().date()}",
                 f"{generate_date().date()}",
                 f"{generate_bool()}",
                 f"{index}",
                 f"{index}"
                 ]
            )

        writer.writerow(["Album"])
        writer.writerow(["id", "name", "song_number", "duration", "artist_id"])

        for index in range(1, 200):
            writer.writerow(
                [f"{index}",
                 f"album{index}",
                 f"{index}",
                 f"{generate_date().time().replace(hour=0).strftime('%H:%M:%S')}",
                 f"{index}"]
            )

        writer.writerow(["Song"])
        writer.writerow(["id", "name", "duration", "artist_id", "album_id"])

        for index in range(1, 200):
            writer.writerow(
                [f"{index}",
                 f"song{index}",
                 f"{generate_date().time().replace(hour=0).strftime('%H:%M:%S')}",
                 f"{index}",
                 f"{index}"]
            )

        writer.writerow(["PlaylistHasSong"])
        writer.writerow(["id", "is_downloaded", "stop_time", "playlist_id", "song_id"])

        for index in range(1, 200):
            writer.writerow(
                [f"{index}",
                 f"{generate_bool()}",
                 f"{generate_date().time().replace(hour=0).strftime('%H:%M:%S')}",
                 f"{index}",
                 f"{index}"]
            )


def generate_date(min_year=1990, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def generate_bool():
    return random.choice([True, False])


def read_from_csv(filename, entity):
    result = {}
    values = []
    headers = ['User', 'SubscriptionType', 'Artist', 'Playlist',
               'Subscription', 'Album', 'Song', 'PlaylistHasSong']

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    entity_index = lines.index(entity)
    header = lines[entity_index + 1].split(',')

    for line_index in range(entity_index + 2, len(lines)):
        if lines[line_index] not in headers:
            line = lines[line_index].split(',')
            values.append(line)
        else:
            break

    result[entity] = (header, values)

    return result


if __name__ == "__main__":
    generate_csv()
