# Azure Formula1 project
Azure Formula1 project is an implementation of the data pipeline which consumes data from the Ergast API and makes F1 drivers/constructors standings available for Business Intelligence consumption. The pipeline infrastructure was built using Microsoft Azure as a backbone with ADLS Gen 2 as Datalake, Databricks/Spark as a data transformation framework, and Data Factory as an orchestrator.

## Table of contents
  * [Data Architecture Diagram](#data-architecture-diagram) 
  * [Ergast API table schema](#ergast-api-table-schema)
  * [How it works](#how-it-works)
      * [Data Project Overview](#data-project-overview)
      * [Data ingestion requirements](#data-ingestion-requirements)
      * [Reporting requirements](#reporting-requirements)
      * [Analysis requirements](#analysis-requirements)
  * [Prerequisites](#prerequisites)      


## Data Architecture Diagram
<img src="Data architecture.png">

## Ergast API Table Schema
<img src="ergast_db.png">

## How it works

### Data Project Overview

These are the files from the Ergast API and the respective file formats that are used in this project, so different approaches are needed from the spark API to read each type of file.

<table>
  <tr>
    <th>File Name</th>
    <th>Format</th>
  </tr>
  <tr>
    <td>Races</td>
    <td>CSV</td>
  </tr>
  <tr>
    <td>Constructors</td>
    <td>Single Line JSON</td>
  </tr>
  <tr>
    <td>Drivers</td>
    <td>Single Line Nested JSON</td>
  </tr>
  <tr>
    <td>Results</td>
    <td>Single Line JSON</td>
  </tr>
  <tr>
    <td>Pit Stops</td>
    <td>Multi Line JSON</td>
  </tr>
  <tr>
    <td>Lap Times</td>
    <td>Split CSV Files</td>
  </tr>
   <tr>
    <td>Qualifying</td>
    <td>Split Multi Line JSON Files</td>
  </tr>

</table>

### Data Ingestion Requirements

* Ingest all 8 files into the data lake.
* Ingested Data must have the schema applied.
* Ingested Data must have audit columns.
* Ingested Data must be stored in columnar format.
* Must be able to analyze ingested data via SQL.
* Ingestion logic must be able to handle the incremental load.
* Join the key information required for reporting to create a new table.
* Join the key information required for analysis to create a new table.
* Transformed tables must have audit columns.

### Reporting requirements

* Driver standings for each year.
* Constructor Standings for each year.

### Analysis Requirements

* Most dominant drivers over the years.
* Most dominant Constructors over the years.
* Visualize the outputs.

## Prerequisites

* Microsoft Azure account
* Azure Databricks Service
* Azure Data Factory
  


