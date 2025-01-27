{{/*
Expand the name of the chart.
*/}}
{{- define "flask-api-pizzaapp-chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "flask-api-pizzaapp-chart.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "flask-api-pizzaapp-chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "flask-api-pizzaapp-chart.labels" -}}
helm.sh/chart: {{ include "flask-api-pizzaapp-chart.chart" . }}
{{ include "flask-api-pizzaapp-chart.selectorLabels" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app: {{ include "flask-api-pizzaapp-chart.name" . }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "flask-api-pizzaapp-chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "flask-api-pizzaapp-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "flask-api-pizzaapp-chart.versionLabel" -}}
{{- $top := index . 0 -}}
{{- $appver := index . 1 -}}
app.kubernetes.io/version: {{ $appver | quote }}
version: {{ $appver | quote }}
{{- end }}

{{/*
Create the name of TLS secret for ingress
*/}}
{{- define "flask-api-pizzaapp-chart.tlsSecretName" -}}
{{- if .Values.ingress.tls.enabled }}
{{- default (printf "%s-cert" .Values.ingress.host | replace "." "-") .Values.ingress.tls.secretName }}
{{- else }}
{{- print "" }}
{{- end }}
{{- end }}
