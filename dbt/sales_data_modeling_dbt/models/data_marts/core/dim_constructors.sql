{{ config(materialized='table') }}

    select

        constructor_id,
        constructor_ref,
        constructor_name as team_name,
        constructor_nationality as team_origin_country,
        constructor_url,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ ref('stg_constructors') }}