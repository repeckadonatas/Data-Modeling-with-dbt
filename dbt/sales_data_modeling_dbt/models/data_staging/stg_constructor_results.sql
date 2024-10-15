{{ config(materialized='view') }}

    select

        constructor_results_id as constructor_result_id,
        race_id,
        constructor_id,
        points,
        status,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'constructor_results') }}