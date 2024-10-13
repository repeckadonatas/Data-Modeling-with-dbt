{{ config(materialized='view') }}

    select

        qualify_id,
        race_id,
        driver_id,
        constructor_id,
        driver_number,
        qualify_position,
        q1_lap_time,
        q2_lap_time,
        q3_lap_time,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'qualifying') }}