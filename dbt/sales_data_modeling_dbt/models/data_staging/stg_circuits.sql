{{ config(materialized='view') }}

    select

        circuit_id,
        circuit_ref,
        circuit_name,
        circuit_location,
        country,
        CAST(latitude as FLOAT) as latitude,
        CAST(longitude as FLOAT) as longitude,
        CAST(altitude as INT) as altitude,
        circuit_url,
        CAST(timestamp as TIMESTAMP WITH TIME ZONE) as timestamp

    from {{ source('raw_f1_data', 'circuits') }}