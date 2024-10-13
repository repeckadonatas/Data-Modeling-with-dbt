{{ config(materialized='view') }}

    select

        lap_times_id as lap_time_id,
        race_id,
        driver_id,
        lap,
        driver_position,
        lap_time,
        milliseconds,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'lap_times') }}