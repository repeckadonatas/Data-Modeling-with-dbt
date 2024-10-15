{{ config(materialized='table') }}

    select
        r.race_year as race_season,
        d.first_name,
        d.last_name,
        SUM(rs.driver_points) as total_points_season
    from {{ ref('stg_drivers') }} d
    join {{ ref('stg_results') }} rs on rs.driver_id = d.driver_id
    join {{ ref('stg_races') }} r on r.race_id = rs.race_id
    group by r.race_year, d.first_name, d.last_name
    order by total_points_season desc