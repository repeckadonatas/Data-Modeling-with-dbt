{{ config(materialized='view') }}

    select

        race_id,
        driver_id,
        pit_stop_number,
        lap,
        time_of_stop,
        stop_duration,
        milliseconds,
        id,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'pit_stops') }}