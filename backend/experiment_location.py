# ---------------- IMPORTS ---------------- #

import googlemaps

from config import (
    GOOGLE_MAPS_API_KEY
)

# ---------------- GOOGLE MAPS CLIENT ---------------- #

gmaps = googlemaps.Client(

    key=GOOGLE_MAPS_API_KEY
)

# ---------------- THERAPIST FINDER ---------------- #

def find_nearby_therapists_by_location(
    location: str
) -> str:

    try:

        # ---------- GEOCODING ---------- #

        geocode_result = gmaps.geocode(
            location
        )

        if not geocode_result:

            return (
                f"No location found for "
                f"{location}."
            )

        lat_lng = geocode_result[0][
            "geometry"
        ]["location"]

        lat = lat_lng["lat"]

        lng = lat_lng["lng"]

        # ---------- PLACES SEARCH ---------- #

        places_result = gmaps.places_nearby(

            location=(lat, lng),

            radius=5000,

            keyword="Psychotherapist"
        )

        results = places_result.get(
            "results",
            []
        )

        if not results:

            return (
                f"No therapists found near "
                f"{location}."
            )

        # ---------- OUTPUT ---------- #

        output = [

            f"Therapists near {location}:"
        ]

        top_results = results[:5]

        for place in top_results:

            name = place.get(
                "name",
                "Unknown"
            )

            address = place.get(
                "vicinity",
                "Address not available"
            )

            # ---------- PHONE DETAILS ---------- #

            phone = (
                "Phone not available"
            )

            try:

                details = gmaps.place(

                    place_id=place[
                        "place_id"
                    ],

                    fields=[
                        "formatted_phone_number"
                    ]
                )

                phone = details.get(

                    "result",

                    {}
                ).get(

                    "formatted_phone_number",

                    "Phone not available"
                )

            except Exception:

                pass

            output.append(

                f"- {name}\n"
                f"  Address: {address}\n"
                f"  Phone: {phone}\n"
            )

        return "\n".join(output)

    except Exception as e:

        return (
            f"Google Maps Error: "
            f"{str(e)}"
        )

# ---------------- TEST ---------------- #

if __name__ == "__main__":

    result = (
        find_nearby_therapists_by_location(
            location="Mumbai"
        )
    )

    print("\nRESULT:\n")

    print(result)