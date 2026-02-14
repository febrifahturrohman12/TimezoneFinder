from fastapi import FastAPI, Query
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

app = FastAPI(
    title="Timezone Finder API",
    description="Find timezone, current time, and GMT offset from geographic coordinates.",
    version="1.0.0",
)

tf = TimezoneFinder()


@app.get("/")
async def root():
    return {"message": "Timezone Finder API is running!"}


@app.get("/timezone")
async def get_timezone(
    lat: float = Query(..., ge=-90, le=90, description="Latitude (-90 to 90)"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude (-180 to 180)"),
):
    """
    Get current time and timezone information based on latitude and longitude.
    """
    timezone_name = tf.timezone_at(lat=lat, lng=lon)

    if not timezone_name:
        return {"error": "Timezone not found for the given coordinates."}

    tz = pytz.timezone(timezone_name)
    current_time = datetime.now(tz)
    gmt_offset_hours = current_time.utcoffset().total_seconds() / 3600

    return {
        "timezone": timezone_name,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "gmt_offset": gmt_offset_hours,
    }
