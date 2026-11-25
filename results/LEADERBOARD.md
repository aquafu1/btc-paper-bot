# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1376 windows, 35748 settled trades, 428 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 714 | 34.2 | 35.3 | $-567.28 | -7.9% | $432.72 | -1.6 | done | can't tell from luck |
| value_ev10 | 1734 | 38.7 | 39.1 | $-826.33 | -4.8% | $173.67 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3574 | 50.8 | 50.1 | $-1057.41 | -3.0% | $-57.41 | -1.8 | done | can't tell from luck |
| value_ev5 | 2610 | 40.4 | 41.1 | $-1318.42 | -5.1% | $-318.42 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2996 | 49.2 | 49.4 | $-1503.06 | -5.0% | $-503.06 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2996 | 50.8 | 50.9 | $-1517.96 | -5.1% | $-517.96 | -2.8 | done | losing for real |
| trend_filter | 2124 | 48.5 | 50.4 | $-1887.96 | -8.9% | $-887.96 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3574 | 49.2 | 50.2 | $-2183.92 | -6.1% | $-1183.92 | -3.7 | done | losing for real |
| coinflip | 5142 | 50.0 | 50.0 | $-2218.95 | -4.3% | $-1218.95 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5142 | 50.1 | 51.3 | $-3203.22 | -6.2% | $-2203.22 | -4.6 | done | losing for real |
| always_up | 5142 | 47.9 | 49.3 | $-3708.81 | -7.2% | $-2708.81 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8875 | 47.9 | 48.8 | $-5175.30 |
| ETH | 9563 | 48.0 | 48.1 | $-5233.79 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
