# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 588 windows, 16293 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1386 | 51.2 | 49.6 | $-199.29 | -1.4% | $800.71 | -0.5 | done | can't tell from luck |
| value_ev20 | 321 | 34.0 | 35.2 | $-276.40 | -8.6% | $723.60 | -1.2 | done | can't tell from luck |
| trend_filter | 946 | 50.3 | 50.9 | $-524.37 | -5.5% | $475.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 766 | 37.9 | 39.4 | $-625.17 | -8.2% | $374.83 | -1.9 | done | can't tell from luck |
| value_ev5 | 1144 | 40.4 | 41.3 | $-721.93 | -6.3% | $278.07 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1653 | 50.8 | 51.0 | $-831.63 | -5.0% | $168.37 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1653 | 49.2 | 49.9 | $-911.23 | -5.5% | $88.77 | -2.2 | done | losing for real |
| coinflip | 2346 | 49.9 | 50.5 | $-1234.08 | -5.3% | $-234.08 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1386 | 48.8 | 51.3 | $-1355.19 | -9.8% | $-355.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2346 | 50.1 | 51.8 | $-1643.02 | -7.0% | $-643.02 | -3.5 | done | losing for real |
| always_up | 2346 | 47.4 | 49.8 | $-2119.15 | -9.0% | $-1119.15 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3696 | 47.9 | 49.2 | $-2598.95 |
| ETH | 4062 | 48.0 | 48.6 | $-2622.21 |
| SOL | 4239 | 47.9 | 48.7 | $-2963.01 |
| XRP | 4296 | 48.5 | 48.6 | $-2257.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
