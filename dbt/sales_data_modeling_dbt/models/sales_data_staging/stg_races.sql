{{ config(materialized='view') }}

    select

        race_id,
        race_year,
        round,
        circuit_id,
        race_name,
        CAST(race_date as DATE),
        race_start_time,
        race_url,
        CAST(fp1_date as DATE),
        fp1_time,
        CAST(fp2_date as DATE),
        fp2_time,
        CAST(fp3_date as DATE),
        fp3_time,
        CAST(qualifying_date as DATE),
        qualifying_start_time,
        CAST(sprint_date as DATE),
        sprint_start_time,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'races') }}