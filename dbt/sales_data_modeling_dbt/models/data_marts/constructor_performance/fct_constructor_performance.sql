{{ config(materialized='table') }}

    select
        r.race_year,
        r.race_name,
        CAST(crt.circuit_name as TEXT),
        c.constructor_name as team_name,
        c.constructor_nationality as team_origin_country,
        cr.points,
        SUM(cr.points) OVER (
            PARTITION BY r.race_year, c.constructor_name
            ) as total_points_season,
        c.constructor_ref
    from {{ ref('stg_constructors') }} c
    join {{ ref('stg_constructor_results') }} cr on cr.constructor_id = c.constructor_id
    join {{ ref('stg_races') }} r on r.race_id = cr.race_id
    join {{ ref('stg_circuits') }} crt on crt.circuit_id = r.circuit_id
    order by 1 DESC, 7 DESC