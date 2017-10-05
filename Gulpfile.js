var gulp = require('gulp'),
    sass = require('gulp-sass'),
    notify = require('gulp-notify'),
    browserSync = require('browser-sync').create(),
    typescript = require('gulp-typescript'),
    imagemin = require('gulp-imagemin'),
    uglify = require('gulp-uglify');


gulp.task('default', ['build', 'watch']);

gulp.task('build', ['scss', 'typescript', 'images', 'js']);   

gulp.task('watch', ['browserSync'], function() {
    gulp.watch('src/scss/**/*.scss', ['style-base', 'style-view']),
    gulp.watch('src/ts/**/*.ts', ['typescript']);
    gulp.watch('src/js/**/*.js', ['js']);
    gulp.watch('../templates/**/*.html').on('change', browserSync.reload);
});

gulp.task('scss', ['style-base', 'style-view']);

gulp.task('style-base', function() {
    console.log('Transpiling base styles.');
    gulp
        .src('src/scss/base.scss')
        .pipe(sass({
            outputStyle: 'compressed'
        }))
        .on('error', notify.onError(function(e) {
            return 'Failed to compile base SCSS' + e.message;
        }))
        .pipe(gulp.dest('css'))
        .pipe(browserSync.stream())
});

gulp.task('style-view', function() {
    console.log('Transpiling views styles.');
    gulp
        .src('static/*.css')
        .pipe(sass({
            outputStyle: 'compressed'
        }))
        .on('error', notify.onError(function(e) {
            return 'Failed to compile views SCSS' + e.message;
        }))
        .pipe(gulp.dest('static/*.css'))
        .pipe(browserSync.stream())
});

gulp.task('typescript', function() {
    console.log('Transpiling typescipt to css');
    gulp
        .src('src/ts/**/*.ts')
        .pipe(typescript({
                noImplicitAny: true
            }))
        .on('error', notify.onError(function(e) {
            return 'Failed to transpiling TS' + e.message;
        }))
        .pipe(gulp.dest('js'))
        .pipe(browserSync.stream())

});

gulp.task('js', function () {
    console.log('Minify js files.');
     gulp
        .src('src/js/**/*.js')
        .pipe(
            uglify()
        )
        .on('error', notify.onError(function(e) {
            return 'Failed to minifying JS' + e.message;
        }))
        .pipe(gulp.dest('js-query'))
        .pipe(browserSync.stream())
});

gulp.task('images', function() {
    console.log('Minifying images');
    gulp
        .src('src/img/**/*.+(png|jpg|jpeg|gif|svg)')
        .pipe(imagemin())
        .on('error', notify.onError(function(e) {
            return 'Failed to minifying img' + e.message;
        }))
        .pipe(gulp.dest('img'));
});

gulp.task('browserSync', function() {
    browserSync.init({
        proxy: 'localhost:8000'
    });
});