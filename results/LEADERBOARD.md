# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 624 windows, 17243 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1460 | 51.4 | 49.5 | $-117.87 | -0.8% | $882.13 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 999 | 50.4 | 50.8 | $-521.18 | -5.2% | $478.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 798 | 38.2 | 39.5 | $-584.18 | -7.3% | $415.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1205 | 40.4 | 41.4 | $-752.82 | -6.2% | $247.18 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1764 | 50.7 | 51.0 | $-872.78 | -4.9% | $127.22 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1764 | 49.3 | 49.9 | $-914.04 | -5.2% | $85.96 | -2.2 | done | losing for real |
| coinflip | 2488 | 50.0 | 50.5 | $-1225.38 | -4.9% | $-225.38 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1460 | 48.6 | 51.4 | $-1453.49 | -10.0% | $-453.49 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2488 | 50.4 | 51.7 | $-1538.98 | -6.2% | $-538.98 | -3.2 | done | losing for real |
| always_up | 2488 | 47.4 | 49.7 | $-2132.16 | -8.6% | $-1132.16 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3915 | 48.2 | 49.2 | $-2446.83 |
| ETH | 4315 | 48.1 | 48.6 | $-2643.17 |
| SOL | 4479 | 47.9 | 48.8 | $-2979.89 |
| XRP | 4534 | 48.5 | 48.5 | $-2307.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
