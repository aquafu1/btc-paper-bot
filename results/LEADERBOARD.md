# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 303 windows, 8093 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 149 | 34.9 | 36.4 | $-144.69 | -9.7% | $855.31 | -0.9 | Sun 3:00 AM | too few trades (149/200) |
| reversal_15m_0.10pct | 802 | 53.1 | 51.9 | $-163.81 | -2.0% | $836.19 | -0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 661 | 52.5 | 51.8 | $-214.76 | -3.2% | $785.24 | -0.9 | done | can't tell from luck |
| value_ev10 | 386 | 38.3 | 40.5 | $-367.53 | -9.5% | $632.47 | -1.6 | done | can't tell from luck |
| value_ev5 | 573 | 39.8 | 42.2 | $-578.83 | -10.1% | $421.17 | -2.1 | done | losing for real |
| trend_filter | 447 | 45.9 | 50.3 | $-596.14 | -13.3% | $403.86 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 661 | 47.5 | 49.9 | $-645.35 | -9.8% | $354.65 | -2.6 | done | losing for real |
| coinflip | 1204 | 50.0 | 50.9 | $-732.42 | -6.1% | $267.58 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 802 | 46.9 | 49.9 | $-818.78 | -10.2% | $181.22 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1204 | 48.8 | 51.3 | $-1082.68 | -9.0% | $-82.68 | -3.2 | done | losing for real |
| always_up | 1204 | 47.3 | 50.3 | $-1229.05 | -10.2% | $-229.05 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1816 | 46.4 | 49.3 | $-1831.26 |
| ETH | 2025 | 47.2 | 48.8 | $-1876.01 |
| SOL | 2101 | 48.2 | 49.4 | $-1653.77 |
| XRP | 2151 | 48.6 | 49.1 | $-1213.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
