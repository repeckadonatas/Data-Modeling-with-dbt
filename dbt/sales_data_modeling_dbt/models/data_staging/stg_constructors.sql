{{ config(materialized='view') }}

    select

        constructor_id,
        constructor_ref,
        constructor_name,
        constructor_nationality,
        constructor_url,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'constructors') }}