# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 499 windows, 13737 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1166 | 51.2 | 49.9 | $-209.28 | -1.8% | $790.72 | -0.6 | done | can't tell from luck |
| value_ev20 | 255 | 33.7 | 35.5 | $-229.21 | -9.0% | $770.79 | -1.1 | done | can't tell from luck |
| trend_filter | 808 | 49.8 | 50.8 | $-537.73 | -6.7% | $462.27 | -1.9 | done | can't tell from luck |
| value_ev10 | 647 | 37.9 | 39.8 | $-550.56 | -8.5% | $449.44 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1388 | 49.9 | 49.7 | $-551.43 | -4.0% | $448.57 | -1.5 | done | can't tell from luck |
| value_ev5 | 955 | 40.1 | 41.6 | $-696.78 | -7.3% | $303.22 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1388 | 50.1 | 51.5 | $-979.97 | -7.1% | $20.03 | -2.7 | done | losing for real |
| coinflip | 1988 | 50.1 | 50.7 | $-1054.08 | -5.3% | $-54.08 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1166 | 48.8 | 51.3 | $-1104.00 | -9.5% | $-104.00 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1988 | 49.7 | 51.6 | $-1491.34 | -7.5% | $-491.34 | -3.5 | done | losing for real |
| always_up | 1988 | 46.1 | 50.2 | $-2431.26 | -12.2% | $-1431.26 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3097 | 47.3 | 49.2 | $-2608.84 |
| ETH | 3438 | 47.9 | 48.7 | $-2362.46 |
| SOL | 3584 | 47.7 | 49.1 | $-2737.34 |
| XRP | 3618 | 48.3 | 48.8 | $-2127.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
