export abstract class DateUtils {
  public static toDate(date: string): Date {
    return new Date(date);
  }

  // Formata para o padrão dd/MM/yyyy
  public static toFormattedDateString(date: Date): string {
    if (typeof date === 'string') {
      date = DateUtils.toDate(date);
    }

    let day = this.toTwoDigits(date.getDate());
    let month = this.toTwoDigits(date.getMonth() + 1);
    let year = date.getFullYear();

    return `${day}/${month}/${year}`;
  }

  // Formata para o padrão hh:mm:ss
  public static toFormattedTimeString(date: Date): string {
    if (typeof date === 'string') {
      date = DateUtils.toDate(date);
    }

    let hours = this.toTwoDigits(date.getHours());
    let minutes = this.toTwoDigits(date.getMinutes());
    let seconds = this.toTwoDigits(date.getSeconds());

    return `${hours}:${minutes}:${seconds}`;
  }

  // Formata para o padrão dd/MM/yyyy hh:mm:ss
  public static toFormattedDateTimeString(date: Date): string {
    if (typeof date === 'string') {
      date = DateUtils.toDate(date);
    }

    return (
      this.toFormattedDateString(date) + ' ' + this.toFormattedTimeString(date)
    );
  }

  // Formata para dois dígitos
  private static toTwoDigits(value: number): string {
    return value.toString().padStart(2, '0');
  }
}
