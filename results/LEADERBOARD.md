# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 420 windows, 11549 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 991 | 50.8 | 50.1 | $-274.34 | -2.8% | $725.66 | -0.9 | done | can't tell from luck |
| value_ev10 | 536 | 39.7 | 40.4 | $-281.49 | -5.3% | $718.51 | -1.0 | done | can't tell from luck |
| value_ev5 | 808 | 41.7 | 42.1 | $-388.73 | -4.8% | $611.27 | -1.2 | done | can't tell from luck |
| trend_filter | 662 | 49.5 | 50.8 | $-422.59 | -6.4% | $577.41 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1168 | 49.1 | 50.0 | $-629.17 | -5.4% | $370.83 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1168 | 50.9 | 51.8 | $-670.04 | -5.7% | $329.96 | -2.1 | done | losing for real |
| coinflip | 1672 | 50.4 | 50.9 | $-789.10 | -4.7% | $210.90 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 991 | 49.2 | 51.8 | $-888.60 | -9.0% | $111.40 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1672 | 49.3 | 51.6 | $-1300.99 | -7.8% | $-300.99 | -3.3 | done | losing for real |
| always_up | 1672 | 45.9 | 50.7 | $-2161.25 | -12.9% | $-1161.25 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2614 | 47.7 | 49.4 | $-1894.53 |
| ETH | 2904 | 47.9 | 49.0 | $-1830.65 |
| SOL | 2991 | 47.6 | 49.5 | $-2525.32 |
| XRP | 3040 | 48.7 | 49.3 | $-1712.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
