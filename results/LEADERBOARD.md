# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 277 windows, 7295 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 718 | 55.0 | 52.2 | $+126.11 | +1.8% | $1126.11 | +0.5 | done | can't tell from luck |
| value_ev20 | 132 | 37.1 | 36.9 | $-49.35 | -3.7% | $950.65 | -0.3 | Sun 7:00 AM | too few trades (132/200) |
| reversal_60m_0.30pct | 586 | 52.4 | 52.2 | $-191.43 | -3.3% | $808.57 | -0.8 | done | can't tell from luck |
| value_ev10 | 353 | 39.1 | 40.8 | $-273.02 | -7.7% | $726.98 | -1.2 | done | can't tell from luck |
| value_ev5 | 516 | 40.9 | 42.4 | $-386.88 | -7.5% | $613.12 | -1.5 | done | can't tell from luck |
| trend_filter | 386 | 46.1 | 50.2 | $-480.31 | -12.4% | $519.69 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 586 | 47.6 | 49.7 | $-516.00 | -8.8% | $484.00 | -2.2 | done | losing for real |
| coinflip | 1100 | 49.8 | 50.9 | $-669.69 | -6.1% | $330.31 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1100 | 49.5 | 51.5 | $-862.85 | -7.8% | $137.15 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 718 | 45.0 | 49.7 | $-949.84 | -13.2% | $50.16 | -3.6 | done | losing for real |
| always_up | 1100 | 47.0 | 50.2 | $-1138.48 | -10.3% | $-138.48 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1632 | 46.8 | 49.5 | $-1544.22 |
| ETH | 1824 | 47.1 | 49.0 | $-1612.79 |
| SOL | 1886 | 48.4 | 49.4 | $-1366.14 |
| XRP | 1953 | 48.9 | 49.1 | $-868.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
