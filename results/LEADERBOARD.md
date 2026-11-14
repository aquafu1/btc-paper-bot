# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 303 windows, 8109 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 151 | 35.1 | 36.5 | $-140.14 | -9.3% | $859.86 | -0.9 | Sun 2:00 AM | too few trades (151/200) |
| reversal_15m_0.10pct | 803 | 53.1 | 51.9 | $-173.81 | -2.2% | $826.19 | -0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 662 | 52.6 | 51.8 | $-200.22 | -3.0% | $799.78 | -0.8 | done | can't tell from luck |
| value_ev10 | 388 | 38.4 | 40.5 | $-362.99 | -9.4% | $637.01 | -1.6 | done | can't tell from luck |
| value_ev5 | 575 | 39.8 | 42.2 | $-574.28 | -10.0% | $425.72 | -2.1 | done | losing for real |
| trend_filter | 447 | 45.9 | 50.3 | $-596.14 | -13.3% | $403.86 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 662 | 47.4 | 49.9 | $-655.35 | -9.9% | $344.65 | -2.6 | done | losing for real |
| coinflip | 1206 | 50.0 | 50.9 | $-737.18 | -6.1% | $262.82 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 803 | 46.9 | 49.9 | $-804.23 | -10.0% | $195.77 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1206 | 48.8 | 51.3 | $-1078.13 | -8.9% | $-78.13 | -3.2 | done | losing for real |
| always_up | 1206 | 47.3 | 50.4 | $-1233.81 | -10.2% | $-233.81 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1826 | 46.5 | 49.3 | $-1783.98 |
| ETH | 2025 | 47.2 | 48.8 | $-1876.01 |
| SOL | 2107 | 48.1 | 49.4 | $-1683.30 |
| XRP | 2151 | 48.6 | 49.1 | $-1213.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
