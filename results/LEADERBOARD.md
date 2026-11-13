# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 277 windows, 7304 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 719 | 54.9 | 52.2 | $+116.11 | +1.6% | $1116.11 | +0.5 | done | can't tell from luck |
| value_ev20 | 133 | 36.8 | 36.9 | $-59.35 | -4.5% | $940.65 | -0.4 | Sun 6:45 AM | too few trades (133/200) |
| reversal_60m_0.30pct | 586 | 52.4 | 52.2 | $-191.43 | -3.3% | $808.57 | -0.8 | done | can't tell from luck |
| value_ev10 | 354 | 39.0 | 40.8 | $-283.02 | -8.0% | $716.98 | -1.3 | done | can't tell from luck |
| value_ev5 | 517 | 40.8 | 42.4 | $-396.88 | -7.7% | $603.12 | -1.5 | done | can't tell from luck |
| trend_filter | 387 | 46.3 | 50.3 | $-476.13 | -12.3% | $523.87 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 586 | 47.6 | 49.7 | $-516.00 | -8.8% | $484.00 | -2.2 | done | losing for real |
| coinflip | 1101 | 49.9 | 50.9 | $-665.51 | -6.0% | $334.49 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1101 | 49.5 | 51.5 | $-858.67 | -7.8% | $141.33 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 719 | 45.1 | 49.7 | $-945.66 | -13.2% | $54.34 | -3.6 | done | losing for real |
| always_up | 1101 | 47.0 | 50.2 | $-1148.48 | -10.4% | $-148.48 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1641 | 46.7 | 49.4 | $-1577.50 |
| ETH | 1824 | 47.1 | 49.0 | $-1612.79 |
| SOL | 1886 | 48.4 | 49.4 | $-1366.14 |
| XRP | 1953 | 48.9 | 49.1 | $-868.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
