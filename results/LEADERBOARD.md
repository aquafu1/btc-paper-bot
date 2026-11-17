# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 576 windows, 15945 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1355 | 51.3 | 49.7 | $-218.07 | -1.6% | $781.93 | -0.6 | done | can't tell from luck |
| value_ev20 | 310 | 33.5 | 35.2 | $-314.56 | -10.1% | $685.44 | -1.4 | done | can't tell from luck |
| trend_filter | 924 | 50.6 | 51.0 | $-474.64 | -5.1% | $525.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 749 | 37.7 | 39.4 | $-677.94 | -9.1% | $322.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1620 | 51.1 | 51.0 | $-726.22 | -4.5% | $273.78 | -1.8 | done | can't tell from luck |
| value_ev5 | 1121 | 40.1 | 41.3 | $-823.91 | -7.3% | $176.09 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1620 | 48.9 | 49.9 | $-996.94 | -6.2% | $3.06 | -2.5 | done | losing for real |
| coinflip | 2297 | 49.8 | 50.5 | $-1236.02 | -5.4% | $-236.02 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1355 | 48.7 | 51.3 | $-1336.85 | -9.9% | $-336.85 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2297 | 50.2 | 51.9 | $-1603.63 | -7.0% | $-603.63 | -3.5 | done | losing for real |
| always_up | 2297 | 47.1 | 49.9 | $-2244.22 | -9.8% | $-1244.22 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3610 | 47.8 | 49.3 | $-2622.63 |
| ETH | 3976 | 48.0 | 48.6 | $-2699.80 |
| SOL | 4151 | 47.8 | 48.8 | $-3073.46 |
| XRP | 4208 | 48.5 | 48.6 | $-2257.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
