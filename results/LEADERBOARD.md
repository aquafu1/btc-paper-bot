# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 430 windows, 11821 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 214 | 34.6 | 36.2 | $-174.42 | -8.2% | $825.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1008 | 50.7 | 50.0 | $-284.25 | -2.8% | $715.75 | -0.9 | done | can't tell from luck |
| value_ev10 | 554 | 39.2 | 40.3 | $-355.64 | -6.4% | $644.36 | -1.3 | done | can't tell from luck |
| trend_filter | 678 | 49.7 | 50.7 | $-409.84 | -6.0% | $590.16 | -1.6 | done | can't tell from luck |
| value_ev5 | 831 | 41.4 | 42.0 | $-441.13 | -5.3% | $558.87 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1196 | 49.2 | 50.0 | $-622.35 | -5.2% | $377.65 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1196 | 50.8 | 51.8 | $-704.13 | -5.9% | $295.87 | -2.1 | done | losing for real |
| coinflip | 1712 | 50.5 | 50.9 | $-777.49 | -4.5% | $222.51 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1008 | 49.3 | 51.8 | $-912.53 | -9.1% | $87.47 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1712 | 49.6 | 51.6 | $-1269.54 | -7.4% | $-269.54 | -3.2 | done | losing for real |
| always_up | 1712 | 46.3 | 50.6 | $-2048.20 | -12.0% | $-1048.20 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2672 | 47.6 | 49.4 | $-2033.86 |
| ETH | 2967 | 48.0 | 48.9 | $-1930.01 |
| SOL | 3069 | 47.9 | 49.4 | $-2330.36 |
| XRP | 3113 | 48.7 | 49.3 | $-1705.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
