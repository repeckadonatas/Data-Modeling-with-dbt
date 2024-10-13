{{ config(materialized='view') }}

    select

        driver_standings_id as driver_standing_id,
        race_id,
        driver_id,
        CAST(driver_points as FLOAT),
        driver_position,
        position_text,
        driver_wins,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'driver_standings') }}