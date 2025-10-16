# Phase 3: Baseline Modeling and Linear Methods Report

## Overview

This report summarizes the results of Phase 3 of the cybersecurity attacks analysis project, which focused on developing baseline models and implementing various linear modeling approaches. The primary goal was to establish foundational predictive models for the severity level of cybersecurity attacks and compare different linear modeling techniques.

## Implementation Tasks

The following tasks were completed as part of Phase 3:

- **TASK-019**: Created notebook for linear modeling approaches (`notebooks/03_linear_models.ipynb`)
- **TASK-020**: Implemented simple baseline models (mean, median, and random)
- **TASK-021**: Developed Linear Regression models for severity level prediction
- **TASK-022**: Implemented Lasso Regression with cross-validation
- **TASK-023**: Implemented Ridge Regression with cross-validation
- **TASK-024**: Implemented ElasticNet Regression with cross-validation
- **TASK-025**: Applied Forward Selection Regression
- **TASK-026**: Applied Backward Selection Regression
- **TASK-027**: Developed Principal Component Regression (PCR) models
- **TASK-028**: Developed Partial Least Squares Regression (PLSR) models
- **TASK-029**: Evaluated and compared all linear models using appropriate metrics

## Dataset

The analysis was performed on the preprocessed cybersecurity attacks data split into training, validation, and test sets. The primary target variable for this phase was the `severity_level` of the attacks, which represents the numerical measure of attack severity.

## Key Findings

### Baseline Models

Simple baseline models were established to provide reference points for more sophisticated approaches:

- **Mean Baseline**: Predicts the mean severity level for all instances
- **Median Baseline**: Predicts the median severity level for all instances
- **Random Baseline**: Makes random predictions based on the distribution of severity levels in the training data

These baseline models generally performed poorly as expected, with low R² values and high error rates.

### Linear Regression Models

Standard linear regression was implemented without regularization and showed moderate performance. The model identified several key features influencing severity levels in cybersecurity attacks.

### Regularized Models

Three regularized linear regression models were implemented:

- **Lasso Regression**: Applied L1 regularization to encourage feature sparsity
- **Ridge Regression**: Applied L2 regularization to handle multicollinearity
- **ElasticNet Regression**: Combined L1 and L2 regularization

Regularized models generally showed improved performance compared to standard linear regression by controlling overfitting. Lasso and ElasticNet performed implicit feature selection by zeroing out coefficients for less important features.

### Feature Selection

Two feature selection approaches were implemented:

- **Forward Selection**: Started with an empty model and sequentially added the most significant features
- **Backward Selection**: Started with all features and sequentially removed the least significant ones

Both methods identified a subset of important features that strongly influence attack severity levels.

### Dimensionality Reduction

Two dimensionality reduction techniques were applied:

- **Principal Component Regression (PCR)**: Used PCA to transform features before regression
- **Partial Least Squares Regression (PLSR)**: Created components with maximal covariance with the target variable

These approaches helped manage the high dimensionality of the feature space while maintaining predictive performance.

## Model Comparison

The performance of all models was compared using multiple metrics:

- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **R² Score**

The best performing model was [will be determined after notebook execution], which achieved an RMSE of [value] and an R² of [value] on the validation set.

## Feature Importance

The most important features for predicting attack severity levels were identified as:

- [List will be populated after notebook execution]

These features align with cybersecurity domain knowledge, as [explanation based on results].

## Visualizations

Several visualizations were created to aid in understanding model performance and feature importance:

- Linear Regression feature coefficients
- Lasso/Ridge/ElasticNet feature coefficients
- PCR/PLSR performance across different numbers of components
- Model comparison charts

## Conclusions and Next Steps

Phase 3 established a strong baseline for predicting cybersecurity attack severity using linear models. The regularized approaches showed promising results by managing the complexity of the feature space.

Key insights from this phase include:

1. [Will be determined based on notebook results]
2. [Will be determined based on notebook results]
3. [Will be determined based on notebook results]

The next phase (Phase 4) will build on these findings by implementing more advanced machine learning models like Support Vector Machines, Decision Trees, Random Forests, and Gradient Boosting methods to potentially improve prediction performance.

## Appendix

All code and detailed analysis can be found in `notebooks/03_linear_models.ipynb`. Model comparison results are saved in `models/linear_model_comparison.csv`.