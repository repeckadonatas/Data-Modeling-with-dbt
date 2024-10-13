{{ config(materialized='view') }}

    select

        pit_stops_id as pit_stop_id,
        race_id,
        driver_id,
        pit_stop_number,
        lap,
        time_of_stop,
        stop_duration,
        milliseconds,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'pit_stops') }}