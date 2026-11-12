# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 154 windows, 3895 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 278 | 60.4 | 53.1 | $+307.57 | +11.1% | $1307.57 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 375 | 56.8 | 52.3 | $+219.94 | +5.9% | $1219.94 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 608 | 52.6 | 51.3 | $-109.50 | -1.8% | $890.50 | -0.5 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 4:45 AM | too few trades (74/200) |
| coinflip | 608 | 51.0 | 50.9 | $-278.16 | -4.6% | $721.84 | -1.2 | done | can't tell from luck |
| value_ev10 | 200 | 37.0 | 40.8 | $-285.12 | -14.3% | $714.88 | -1.8 | done | can't tell from luck |
| trend_filter | 199 | 41.2 | 49.2 | $-388.62 | -19.5% | $611.38 | -2.8 | Thu 8:00 AM | too few trades (199/200) |
| value_ev5 | 292 | 38.4 | 42.4 | $-411.94 | -14.1% | $588.06 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 278 | 39.6 | 49.3 | $-621.30 | -22.3% | $378.70 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 375 | 43.2 | 50.0 | $-628.84 | -16.8% | $371.16 | -3.3 | done | losing for real |
| always_up | 608 | 46.4 | 50.1 | $-729.00 | -12.0% | $271.00 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 839 | 46.0 | 49.7 | $-868.50 |
| ETH | 964 | 45.6 | 48.9 | $-1062.50 |
| SOL | 1026 | 48.1 | 48.9 | $-793.27 |
| XRP | 1066 | 50.4 | 49.2 | $-344.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
