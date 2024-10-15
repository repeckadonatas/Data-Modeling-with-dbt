{{ config(materialized='table') }}

    select
        r.race_year,
        r.race_name,
        d.driver_code,
        d.first_name || ' ' || d.last_name as drivers_full_name,
        rs.official_position,
        rs.driver_points,
        rs.finish_time,
        rs.fastest_lap,
        rs.fastest_lap_time,
        rs.fastest_lap_speed,
        s.status,
        c.constructor_name as driver_team,
        c.constructor_ref as team_ref
    from {{ ref('stg_results') }} rs
    join {{ ref('stg_races') }} r on r.race_id = rs.race_id
    join {{ ref('stg_drivers') }} d on d.driver_id = rs.driver_id
    join {{ ref('stg_constructors') }} c on c.constructor_id = rs.constructor_id
    join {{ ref('stg_status') }} s on s.status_id = rs.status_id
