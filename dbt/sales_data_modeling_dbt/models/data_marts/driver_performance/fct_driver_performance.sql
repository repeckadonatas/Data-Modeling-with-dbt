{{ config(materialized='table') }}

    select
        r.race_year,
        r.race_name,
        CAST(cr.circuit_name as TEXT),
        d.driver_code,
        d.first_name || ' ' || d.last_name as drivers_full_name,
        c.constructor_name as driver_team,
        CASE
            WHEN rs.official_position = 1 THEN '1st'
            WHEN rs.official_position = 2 THEN '2nd'
            WHEN rs.official_position = 3 THEN '3rd'
        END podium_position,
        rs.driver_points,
        rs.official_position
    from {{ ref('stg_results') }} rs
    join {{ ref('stg_races') }} r on r.race_id = rs.race_id
    join {{ ref('stg_drivers') }} d on d.driver_id = rs.driver_id
    join {{ ref('stg_constructors') }} c on c.constructor_id = rs.constructor_id
    join {{ ref('stg_circuits') }} cr on cr.circuit_id = r.circuit_id
    order by 7, 1 DESC