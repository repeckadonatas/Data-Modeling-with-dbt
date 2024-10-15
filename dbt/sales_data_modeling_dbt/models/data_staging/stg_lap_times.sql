{{ config(materialized='view') }}

    select

        race_id,
        driver_id,
        lap,
        driver_position,
        lap_time,
        milliseconds,
        id,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'lap_times') }}