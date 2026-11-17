# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 624 windows, 17249 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1460 | 51.4 | 49.5 | $-117.87 | -0.8% | $882.13 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 999 | 50.4 | 50.8 | $-521.18 | -5.2% | $478.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 798 | 38.2 | 39.5 | $-584.18 | -7.3% | $415.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1206 | 40.5 | 41.4 | $-743.88 | -6.2% | $256.12 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1765 | 50.7 | 51.0 | $-863.85 | -4.9% | $136.15 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1765 | 49.3 | 49.9 | $-924.04 | -5.2% | $75.96 | -2.2 | done | losing for real |
| coinflip | 2489 | 50.0 | 50.5 | $-1216.44 | -4.9% | $-216.44 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1460 | 48.6 | 51.4 | $-1453.49 | -10.0% | $-453.49 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2489 | 50.4 | 51.7 | $-1530.04 | -6.1% | $-530.04 | -3.2 | done | losing for real |
| always_up | 2489 | 47.4 | 49.7 | $-2123.23 | -8.5% | $-1123.23 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3921 | 48.2 | 49.2 | $-2412.16 |
| ETH | 4315 | 48.1 | 48.6 | $-2643.17 |
| SOL | 4479 | 47.9 | 48.8 | $-2979.89 |
| XRP | 4534 | 48.5 | 48.5 | $-2307.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
