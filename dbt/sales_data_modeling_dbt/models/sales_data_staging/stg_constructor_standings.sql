{{ config(materialized='view') }}

    select

        constructor_standings_id as constructor_standing_id,
        race_id,
        constructor_id,
        constructor_points,
        constructor_position,
        position_text,
        constructor_wins,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'constructor_standings') }}