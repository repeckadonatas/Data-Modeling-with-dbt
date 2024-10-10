{{ config(materialized='view') }}

    select

        driver_id,
        driver_ref,
        driver_number,
        driver_code,
        first_name,
        last_name,
        CAST(date_of_birth as DATE) as date_of_birth,
        driver_nationality,
        driver_url,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'drivers') }}