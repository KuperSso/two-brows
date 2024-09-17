FROM python:3.12-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system app && adduser --system --group app
                                                                            
ENV APP_HOME=/home/app
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

COPY ./backend $APP_HOME

RUN chown -R app:app $APP_HOME

USER app
