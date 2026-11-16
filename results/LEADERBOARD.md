# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 520 windows, 14342 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1222 | 51.2 | 49.8 | $-182.73 | -1.5% | $817.27 | -0.5 | done | can't tell from luck |
| value_ev20 | 269 | 34.6 | 35.6 | $-184.33 | -6.9% | $815.67 | -0.9 | done | can't tell from luck |
| value_ev10 | 670 | 38.1 | 39.7 | $-516.39 | -7.7% | $483.61 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1453 | 49.8 | 49.6 | $-567.40 | -3.9% | $432.60 | -1.5 | done | can't tell from luck |
| trend_filter | 840 | 49.4 | 50.7 | $-577.53 | -6.9% | $422.47 | -2.0 | done | losing for real |
| value_ev5 | 994 | 39.9 | 41.5 | $-731.28 | -7.4% | $268.72 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1453 | 50.2 | 51.6 | $-989.76 | -6.8% | $10.24 | -2.7 | done | losing for real |
| coinflip | 2073 | 50.1 | 50.7 | $-1090.41 | -5.3% | $-90.41 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1222 | 48.8 | 51.4 | $-1147.24 | -9.4% | $-147.24 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2073 | 49.4 | 51.6 | $-1654.96 | -8.0% | $-654.96 | -3.8 | done | losing for real |
| always_up | 2073 | 46.6 | 50.1 | $-2318.59 | -11.2% | $-1318.59 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3248 | 47.4 | 49.2 | $-2634.69 |
| ETH | 3579 | 48.0 | 48.7 | $-2390.38 |
| SOL | 3738 | 47.6 | 49.0 | $-2759.53 |
| XRP | 3777 | 48.4 | 48.8 | $-2176.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
