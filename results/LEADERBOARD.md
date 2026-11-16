# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 550 windows, 15268 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1306 | 51.4 | 49.7 | $-218.15 | -1.7% | $781.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 300 | 33.0 | 35.2 | $-354.01 | -11.8% | $645.99 | -1.6 | done | can't tell from luck |
| trend_filter | 889 | 50.6 | 51.0 | $-469.63 | -5.3% | $530.37 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1546 | 49.6 | 49.7 | $-741.16 | -4.8% | $258.84 | -1.9 | done | can't tell from luck |
| value_ev10 | 722 | 36.8 | 39.4 | $-797.00 | -11.0% | $203.00 | -2.5 | done | losing for real |
| value_ev5 | 1074 | 39.3 | 41.2 | $-974.23 | -9.1% | $25.77 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1546 | 50.4 | 51.2 | $-1031.19 | -6.7% | $-31.19 | -2.7 | done | losing for real |
| coinflip | 2193 | 49.9 | 50.6 | $-1272.18 | -5.8% | $-272.18 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1306 | 48.6 | 51.2 | $-1324.37 | -10.1% | $-324.37 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2193 | 50.2 | 51.8 | $-1589.88 | -7.2% | $-589.88 | -3.5 | done | losing for real |
| always_up | 2193 | 46.7 | 49.9 | $-2438.94 | -11.1% | $-1438.94 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3451 | 47.5 | 49.2 | $-2851.07 |
| ETH | 3804 | 47.9 | 48.6 | $-2767.19 |
| SOL | 3992 | 47.7 | 48.7 | $-3101.57 |
| XRP | 4021 | 48.4 | 48.6 | $-2490.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
