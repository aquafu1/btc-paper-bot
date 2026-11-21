# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 968 windows, 26825 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| value_ev10 | 1225 | 38.0 | 39.0 | $-729.05 | -6.0% | $270.95 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2738 | 51.2 | 50.5 | $-747.56 | -2.7% | $252.44 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2288 | 50.3 | 49.8 | $-867.42 | -3.8% | $132.58 | -1.8 | done | can't tell from luck |
| trend_filter | 1604 | 50.1 | 50.9 | $-1051.52 | -6.6% | $-51.52 | -2.7 | done | losing for real |
| value_ev5 | 1856 | 39.8 | 40.9 | $-1102.06 | -5.9% | $-102.06 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2288 | 49.7 | 50.9 | $-1659.74 | -7.3% | $-659.74 | -3.5 | done | losing for real |
| coinflip | 3864 | 50.2 | 50.3 | $-1762.70 | -4.6% | $-762.70 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2738 | 48.8 | 50.3 | $-1933.65 | -7.1% | $-933.65 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3864 | 50.9 | 51.6 | $-1994.49 | -5.2% | $-994.49 | -3.3 | done | losing for real |
| always_up | 3864 | 46.8 | 49.6 | $-3849.88 | -10.0% | $-2849.88 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6110 | 48.2 | 49.1 | $-3497.56 |
| ETH | 6665 | 48.1 | 48.5 | $-4187.09 |
| SOL | 7006 | 48.2 | 48.6 | $-3874.91 |
| XRP | 7044 | 48.2 | 48.4 | $-4358.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
