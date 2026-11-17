# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 606 windows, 16740 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1415 | 51.2 | 49.6 | $-187.18 | -1.3% | $812.82 | -0.5 | done | can't tell from luck |
| value_ev20 | 326 | 34.4 | 35.2 | $-234.70 | -7.2% | $765.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 782 | 38.2 | 39.4 | $-547.21 | -7.0% | $452.79 | -1.6 | done | can't tell from luck |
| trend_filter | 965 | 50.3 | 51.0 | $-547.30 | -5.7% | $452.70 | -1.8 | done | can't tell from luck |
| value_ev5 | 1173 | 40.5 | 41.2 | $-677.73 | -5.8% | $322.27 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1708 | 50.7 | 50.9 | $-812.00 | -4.8% | $188.00 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1708 | 49.3 | 50.0 | $-939.56 | -5.5% | $60.44 | -2.3 | done | losing for real |
| coinflip | 2416 | 50.0 | 50.5 | $-1198.74 | -5.0% | $-198.74 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1415 | 48.8 | 51.3 | $-1357.97 | -9.6% | $-357.97 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2416 | 50.2 | 51.8 | $-1601.03 | -6.6% | $-601.03 | -3.4 | done | losing for real |
| always_up | 2416 | 47.0 | 49.8 | $-2340.25 | -9.7% | $-1340.25 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3808 | 48.0 | 49.2 | $-2499.68 |
| ETH | 4175 | 48.0 | 48.6 | $-2731.78 |
| SOL | 4350 | 47.9 | 48.7 | $-2945.50 |
| XRP | 4407 | 48.5 | 48.6 | $-2266.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
