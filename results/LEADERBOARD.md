# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1122 windows, 31049 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 592 | 34.6 | 35.1 | $-346.72 | -5.9% | $653.28 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3130 | 51.2 | 50.4 | $-819.07 | -2.6% | $180.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1450 | 38.2 | 39.2 | $-862.30 | -5.9% | $137.70 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2634 | 49.7 | 49.4 | $-1108.41 | -4.2% | $-108.41 | -2.2 | done | losing for real |
| value_ev5 | 2194 | 40.1 | 41.1 | $-1237.43 | -5.6% | $-237.43 | -2.2 | done | losing for real |
| trend_filter | 1845 | 49.2 | 50.4 | $-1398.45 | -7.6% | $-398.45 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2634 | 50.3 | 51.1 | $-1674.58 | -6.4% | $-674.58 | -3.3 | done | losing for real |
| coinflip | 4480 | 50.4 | 50.2 | $-1747.87 | -3.9% | $-747.87 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3130 | 48.8 | 50.2 | $-2087.28 | -6.7% | $-1087.28 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4480 | 50.4 | 51.4 | $-2568.66 | -5.7% | $-1568.66 | -4.0 | done | losing for real |
| always_up | 4480 | 47.7 | 49.3 | $-3404.54 | -7.6% | $-2404.54 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7119 | 48.4 | 49.0 | $-3581.22 |
| ETH | 7696 | 48.2 | 48.4 | $-4605.11 |
| SOL | 8077 | 48.1 | 48.4 | $-4491.63 |
| XRP | 8157 | 48.2 | 48.2 | $-4577.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
