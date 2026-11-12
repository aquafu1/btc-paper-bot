# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 182 windows, 4640 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 452 | 57.7 | 52.4 | $+324.24 | +7.2% | $1324.24 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 341 | 59.5 | 53.1 | $+311.62 | +9.1% | $1311.62 | +1.8 | done | can't tell from luck |
| value_ev20 | 87 | 33.3 | 36.6 | $-143.13 | -16.5% | $856.87 | -1.3 | Sun 4:30 AM | too few trades (87/200) |
| momentum_5m_0.00pct | 720 | 51.5 | 51.3 | $-259.35 | -3.6% | $740.65 | -1.0 | done | can't tell from luck |
| value_ev10 | 233 | 36.5 | 40.6 | $-349.22 | -15.0% | $650.78 | -2.0 | done | losing for real |
| coinflip | 720 | 50.4 | 50.9 | $-381.05 | -5.3% | $618.95 | -1.5 | done | can't tell from luck |
| trend_filter | 231 | 41.6 | 49.3 | $-428.40 | -18.5% | $571.60 | -2.8 | done | losing for real |
| value_ev5 | 343 | 38.2 | 42.4 | $-486.08 | -14.2% | $513.92 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 341 | 40.5 | 49.0 | $-710.36 | -20.8% | $289.64 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 452 | 42.3 | 49.7 | $-813.94 | -18.0% | $186.06 | -3.9 | done | losing for real |
| always_up | 720 | 46.4 | 50.0 | $-838.97 | -11.7% | $161.03 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1013 | 45.7 | 49.4 | $-1045.38 |
| ETH | 1156 | 45.9 | 48.8 | $-1294.50 |
| SOL | 1204 | 47.5 | 49.0 | $-1094.74 |
| XRP | 1267 | 50.2 | 49.1 | $-340.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
