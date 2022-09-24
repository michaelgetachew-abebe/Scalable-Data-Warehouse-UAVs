/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml
    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

with fast_vehicles as (
    SELECT *
    from trajectories 
    ORDER BY avg_speed DESC
    LIMIT 100
)
