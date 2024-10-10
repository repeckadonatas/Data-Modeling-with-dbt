{{ config(materialized='view') }}

    select

        status_id,
        status,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'status') }}