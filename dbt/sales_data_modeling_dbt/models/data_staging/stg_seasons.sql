{{ config(materialized='view') }}

    select

        CAST(year as INT) as year,
        url,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'seasons') }}