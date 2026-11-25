# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1341 windows, 35253 settled trades, 398 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 694 | 34.3 | 35.4 | $-528.07 | -7.6% | $471.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1698 | 38.8 | 39.2 | $-816.38 | -4.8% | $183.62 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3529 | 50.9 | 50.2 | $-995.58 | -2.8% | $4.42 | -1.7 | done | can't tell from luck |
| value_ev5 | 2563 | 40.5 | 41.1 | $-1312.23 | -5.1% | $-312.23 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2963 | 49.3 | 49.4 | $-1457.18 | -4.9% | $-457.18 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2963 | 50.7 | 50.9 | $-1541.46 | -5.2% | $-541.46 | -2.9 | done | losing for real |
| trend_filter | 2098 | 48.7 | 50.5 | $-1797.74 | -8.6% | $-797.74 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3529 | 49.1 | 50.2 | $-2236.71 | -6.3% | $-1236.71 | -3.8 | done | losing for real |
| coinflip | 5072 | 49.9 | 50.1 | $-2320.74 | -4.6% | $-1320.74 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5072 | 50.3 | 51.4 | $-3037.55 | -6.0% | $-2037.55 | -4.4 | done | losing for real |
| always_up | 5072 | 47.9 | 49.3 | $-3664.55 | -7.2% | $-2664.55 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8635 | 47.9 | 48.9 | $-5233.86 |
| ETH | 9308 | 48.2 | 48.2 | $-4890.08 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
