{{ config(materialized='table') }}

    select
        r.race_year as race_season,
        c.constructor_name,
        SUM(cs.points) as total_points_season
    from {{ ref('stg_constructors') }} c
    join {{ ref('stg_constructor_results') }} cs on cs.constructor_id = c.constructor_id
    join {{ ref('stg_races') }} r on r.race_id = cs.race_id
    group by r.race_year, c.constructor_name
    order by total_points_season desc