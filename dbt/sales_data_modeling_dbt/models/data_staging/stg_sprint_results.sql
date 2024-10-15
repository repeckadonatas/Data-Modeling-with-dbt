{{ config(materialized='view') }}

    select

        sprint_result_id,
        race_id,
        driver_id,
        constructor_id,
        driver_number,
        grid_position,
        official_position,
        position_text,
        position_order,
        driver_points,
        laps_completed,
        finish_time,
        time_milliseconds as milliseconds,
        fastest_lap,
        fastest_lap_time,
        status_id,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'sprint_results') }}